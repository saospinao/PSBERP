import sys
import json
import os
from datetime import datetime

try:
    # Leer JSON desde stdin
    data = json.load(sys.stdin)
    
    session_id = data.get('session_id', '')
    prompt = data.get('prompt', '').lower()
    cwd = data.get('cwd', '')
    
    # Construir ruta relativa al log desde el cwd
    log_file = os.path.join(cwd, '.claude', 'logs', 'active_agents.json')
    
    # Crear directorio si no existe
    log_dir = os.path.dirname(log_file)
    os.makedirs(log_dir, exist_ok=True)
    
    # Lista completa de agentes disponibles
    agent_identifiers = {
        'agents:po': 'PO',
        'agents:sm': 'SM',
        'agents:pm': 'PM',
        'agents:analyst': 'ANALYST',
        'agents:architect': 'ARCHITECT',
        'agents:dev': 'DEV',
        'agents:backend': 'BACKEND',
        'agents:frontend': 'FRONTEND',
        'agents:qa': 'QA',
        'agents:ux-expert': 'UX-EXPERT',
        'agents:bmad-master': 'BMAD-MASTER',
        'agents:bmad-orchestrator': 'BMAD-ORCHESTRATOR'
    }
    
    # Detectar si se está invocando un agente
    agent_type = None
    for identifier, agent_name in agent_identifiers.items():
        if identifier in prompt or f'/bmad:{identifier}' in prompt:
            agent_type = agent_name
            break
    
    if agent_type and session_id:
        # Leer log existente
        active_agents = {}
        if os.path.exists(log_file):
            try:
                with open(log_file, 'r', encoding='utf-8') as f:
                    active_agents = json.load(f)
            except:
                active_agents = {}
        
        # Actualizar o agregar la sesión con el agente actual
        active_agents[session_id] = {
            'agent': agent_type,
            'timestamp': datetime.now().isoformat(),
            'last_prompt': prompt[:100]  # Guardar inicio del prompt para debug
        }
        
        # Guardar log actualizado
        with open(log_file, 'w', encoding='utf-8') as f:
            json.dump(active_agents, f, indent=2, ensure_ascii=False)

except Exception as e:
    # En caso de error, no bloquear la operación
    pass
