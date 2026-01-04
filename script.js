let equations = [{ id: 1, value: '' }];
let params = {};
let layout = {
    margin: { t: 0, r: 0, b: 0, l: 0 },
    xaxis: {
        zeroline: true,
        gridcolor: '#eee',
        zerolinecolor: '#333'
    },
    yaxis: {
        zeroline: true,
        gridcolor: '#eee',
        zerolinecolor: '#333'
    },
    showlegend: false,
    hovermode: 'closest'
};
let config = { responsive: true, displayModeBar: false };

// Initial Setup
let currentXMin = -10;
let currentXMax = 10;

document.addEventListener('DOMContentLoaded', () => {
    addEquationInput();
    const chart = document.getElementById('chart-container');

    Plotly.newPlot(chart, [], layout, config).then(() => {
        // Listen for zoom/pan events
        chart.on('plotly_relayout', (eventdata) => {
            // Check if X-axis changed
            if (eventdata['xaxis.range[0]'] && eventdata['xaxis.range[1]']) {
                currentXMin = eventdata['xaxis.range[0]'];
                currentXMax = eventdata['xaxis.range[1]'];
                debouncePlot();
            } else if (eventdata['xaxis.autorange']) {
                // Reset to default if user double clicks or resets
                currentXMin = -10;
                currentXMax = 10;
                debouncePlot();
            }
        });
    });
});

// Add a new equation input row
function addEquationInput(defaultValue = '') {
    const list = document.getElementById('equation-list');
    const id = Date.now();

    const div = document.createElement('div');
    div.className = 'equation-item';
    div.dataset.id = id;

    // Assign a random color for this equation (simple hash)
    const color = hsl(id % 360);

    div.innerHTML = `
        <div class="color-indicator" style="background-color: ${color}"></div>
        <input class="equation-input" 
               placeholder="Expression (e.g. x^2)" 
               value="${defaultValue}"
               oninput="onEquationChange(${id}, this.value)">
        <button class="remove-btn" onclick="removeEquation(${id})">&times;</button>
    `;

    list.appendChild(div);
    equations.push({ id, value: defaultValue, color });

    // Auto-focus the new input
    div.querySelector('input').focus();
}

function removeEquation(id) {
    equations = equations.filter(eq => eq.id !== id);
    const el = document.querySelector(`.equation-item[data-id='${id}']`);
    if (el) el.remove();
    updatePlot();
}

function onEquationChange(id, value) {
    const eq = equations.find(e => e.id === id);
    if (eq) eq.value = value;
    debouncePlot();
}

// Debounce Utility to avoid spamming the API
let debounceTimer;
function debouncePlot() {
    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(updatePlot, 300);
}

function hsl(h) {
    return `hsl(${h}, 70%, 50%)`;
}

// Update the parameter value (from slider)
function updateParam(name, value) {
    params[name] = parseFloat(value);
    document.getElementById(`val-${name}`).innerText = value;
    debouncePlot();
}

async function updatePlot() {
    // Collect non-empty equations
    const activeEqs = equations.filter(e => e.value.trim() !== '').map(e => e.value);

    if (activeEqs.length === 0) {
        Plotly.react('chart-container', [], layout, config);
        renderSliders([]);
        return;
    }

    const widthPx = document.getElementById('chart-container').clientWidth;

    try {
        const response = await fetch('/plot', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                equations: activeEqs,
                params: params,
                x_min: currentXMin,
                x_max: currentXMax,
                width_px: Math.floor(widthPx || 800)
            })
        });

        const data = await response.json();

        if (data.plots) {
            const traces = data.plots.map((p, index) => {
                // Find original color or assign new
                const eqIndex = equations.findIndex(e => e.value === p.expr);
                const color = equations[eqIndex >= 0 ? eqIndex : 0]?.color || '#000';

                return {
                    x: p.x,
                    y: p.y,
                    mode: 'lines',
                    type: 'scatter',
                    line: { color: color, width: 3 },
                    name: p.expr,
                    hovertemplate: `<b>${p.expr}</b><br>x: %{x:.3f}<br>y: %{y:.3f}<extra></extra>`
                };
            });

            // Retain zoom/pan state by pulling current layout
            const graphDiv = document.getElementById('chart-container');
            const currentLayout = Object.assign({}, graphDiv.layout || layout);

            Plotly.react('chart-container', traces, currentLayout, config);

            // Update sliders based on what the detected params
            renderSliders(data.detected_params);
        }

    } catch (e) {
        console.error("Plotting error:", e);
    }
}

// Dynamically render sliders
function renderSliders(detectedParams) {
    const container = document.getElementById('slider-list');

    detectedParams.forEach(param => {
        if (!document.getElementById(`slider-${param}`)) {
            // New param found
            if (!(param in params)) params[param] = 1.0; // Default value

            const div = document.createElement('div');
            div.className = 'slider-item';
            div.id = `wrapper-${param}`;
            div.innerHTML = `
                <div class="slider-header">
                    <span>${param}</span>
                    <span id="val-${param}">${params[param]}</span>
                </div>
                <input type="range" id="slider-${param}" class="slider-input"
                       min="-10" max="10" step="0.1" value="${params[param]}"
                       oninput="updateParam('${param}', this.value)">
            `;
            container.appendChild(div);
        }
    });
}
