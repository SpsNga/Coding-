import sympy as sp
import numpy as np
import re
import warnings

def evaluate_expressions(equations: list[str], params: dict[str, float], x_min: float = -10, x_max: float = 10, num_points: int = 500):
    """
    Evaluates a list of equations with dynamic range support.
    """
    
    x = sp.symbols('x')
    plot_data = []
    all_free_symbols = set()
    
    # Standard math functions to support in numpy
    # We map sympy functions to numpy functions for fast evaluation
    modules = [{'sin': np.sin, 'cos': np.cos, 'tan': np.tan, 
                'exp': np.exp, 'log': np.log, 'sqrt': np.sqrt,
                'pi': np.pi, 'E': np.e}, 'numpy']

    x_vals = np.linspace(x_min, x_max, num_points)

    # Context manager to suppress math/numpy warnings (overflows, div by zero)
    # This prevents console spam and keeps the log clean
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        np.seterr(all='ignore')

        for eq_str in equations:
            if not eq_str.strip():
                continue
                
            try:
                # Clean up the equation string slightly
                if '=' in eq_str:
                    parts = eq_str.split('=')
                    eq_to_parse = parts[-1] 
                else:
                    eq_to_parse = eq_str

                # Parse the expression
                expr = sp.sympify(eq_to_parse)
                
                # Find free symbols
                free_syms = expr.free_symbols
                params_needed = {s.name for s in free_syms if s.name != 'x'}
                all_free_symbols.update(params_needed)
                
                # Substitute known parameters
                subs_dict = {sp.symbols(k): v for k, v in params.items() if k in params_needed}
                expr_sub = expr.subs(subs_dict)
                
                # Check remaining symbols
                remaining_syms = {s.name for s in expr_sub.free_symbols if s.name != 'x'}
                
                y_vals = []
                if not remaining_syms:
                    f = sp.lambdify(x, expr_sub, modules=modules)
                    
                    try:
                        y_vals = f(x_vals)
                        # Handle scalar output
                        if np.isscalar(y_vals):
                            y_vals = np.full_like(x_vals, y_vals)
                            
                        # Robust cleaning for heavy expressions
                        y_vals = np.array(y_vals, dtype=float)
                        
                        # Clip EXTREMELY large values to avoid JSON issues, 
                        # but keep them finite so they might show as "off screen"
                        # json standard usually supports up to 1e308 (double), but let's be safe
                        max_val = 1e150 
                        y_vals = np.where(np.abs(y_vals) > max_val, np.nan, y_vals)
                        
                        y_list = y_vals.tolist()
                        # Final sanitizer: NaN/Inf -> None
                        y_vals = [None if (val is None or np.isnan(val) or np.isinf(val)) else val for val in y_list]

                    except (OverflowError, ValueError, RuntimeWarning):
                        # Capture specific math errors during evaluation
                        y_vals = [None] * len(x_vals)
                    except Exception:
                         y_vals = [None] * len(x_vals)
                
                plot_data.append({
                    "expr": eq_str,
                    "x": x_vals.tolist() if y_vals else [],
                    "y": y_vals,
                    "error": None
                })

            except Exception as e:
                plot_data.append({
                    "expr": eq_str,
                    "x": [],
                    "y": [],
                    "error": str(e)
                })

    return {
        "plots": plot_data,
        "detected_params": list(all_free_symbols)
    }
