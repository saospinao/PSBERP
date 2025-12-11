import sys
import json
import os

try:
    # Leer JSON desde stdin
    data = json.load(sys.stdin)

    # Obtener información del archivo y sesión
    file_path = data.get('tool_input', {}).get('file_path', '')
    extension = os.path.splitext(file_path)[1].lower() if file_path else ''
    session_id = data.get('session_id', '')
    cwd = data.get('cwd', '')

    # Construir ruta relativa al log desde el cwd
    log_file = os.path.join(cwd, '.claude', 'logs', 'active_agents.json')

    # Agentes que solo pueden escribir markdown
    MARKDOWN_ONLY_AGENTS = ['PO', 'SM', 'PM', 'ANALYST', 'ARCHITECT', 'UX-EXPERT']

    # Verificar si la sesión actual tiene un agente activo
    if session_id and os.path.exists(log_file):
        try:
            with open(log_file, 'r', encoding='utf-8') as f:
                active_agents = json.load(f)
            
            # Si la sesión actual tiene un agente activo
            if session_id in active_agents:
                agent_type = active_agents[session_id]['agent']
                
                # Si el agente está en la lista de solo markdown
                if agent_type in MARKDOWN_ONLY_AGENTS:
                    # Solo permitir archivos markdown
                    if extension != '.md':
                        result = {
                            "hookSpecificOutput": {
                                "hookEventName": "PreToolUse",
                                "permissionDecision": "deny",
                                "permissionDecisionReason": f"⛔ El agente de tipo {agent_type} solo puede redactar archivos markdown"
                            }
                        }
                        print(json.dumps(result))
                        sys.exit(0)
        except:
            # Si hay error leyendo el log, permitir la operación
            pass

    # Si no está bloqueado, permitir la operación (no imprimir nada)
except Exception as e:
    # En caso de error, permitir la operación
    pass
