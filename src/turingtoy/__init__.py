from typing import (
    Dict,
    List,
    Optional,
    Tuple,
)

import poetry_version

__version__ = poetry_version.extract(source_file=__file__)


def execute_turing_machine(
    turing_machine: Dict,
    input_string: str,
    max_steps: Optional[int] = None,
) -> Tuple[str, List[Dict[str, any]], bool]:
    # Initial setup
    blank_symbol = turing_machine['blank']
    initial_state = turing_machine['start state']
    accepting_states = set(turing_machine['final states'])
    transition_table = turing_machine['table']
    
    tape = list(input_string)
    head_position = 0
    current_state = initial_state
    
    history = []
    
    step_counter = 0
    
    def log_state(state, read_symbol, head_pos, tape_content, action):
        history.append({
            'state': state,
            'reading': read_symbol,
            'position': head_pos,
            'memory': ''.join(tape_content),
            'transition': action
        })
    
    while True:
        if head_position < 0 or head_position >= len(tape):
            current_read = blank_symbol
        else:
            current_read = tape[head_position]
        
        log_state(current_state, current_read, head_position, tape.copy(), transition_table.get(current_state, {}).get(current_read, {}))
        
        if current_state in accepting_states:
            return ''.join(tape).rstrip(blank_symbol), history, True
        
        state_transitions = transition_table.get(current_state, {})
        if current_read not in state_transitions:
            return ''.join(tape).rstrip(blank_symbol), history, False
        
        action = state_transitions[current_read]
        
        if isinstance(action, str):
            if action == 'R':
                head_position += 1
            elif action == 'L':
                head_position -= 1
        else:
            if 'write' in action:
                if head_position < 0:
                    tape.insert(0, action['write'])
                    head_position = 0
                elif head_position >= len(tape):
                    tape.append(action['write'])
                else:
                    tape[head_position] = action['write']
            
            if 'R' in action:
                current_state = action['R']
                head_position += 1
            elif 'L' in action:
                current_state = action['L']
                head_position -= 1
        
        step_counter += 1
        if max_steps is not None and step_counter >= max_steps:
            return ''.join(tape).rstrip(blank_symbol), history, False
