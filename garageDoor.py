import random

# the atoms of the system
CLOSED = 'closed'
OPENING = 'opening'
OPEN = 'open'
CLOSING = 'closing'

# the events
BUTTON_PRESSED = 'button pressed'
LIMIT_TRIPPED = 'limit tripped'

# the states of the system
x0 = 'x0'
x1 = 'x1'
x2 = 'x2'
x3 = 'x3'
S = [x0, x1, x2, x3]

# the state transition relation
# OPENING hasd a 20% chance of jumping directly to CLOSING by defn.
R =   { x0: dict({x1: 1.0}),
	x1: dict({x2: 0.8, x3: 0.2}),
	x2: dict({x3: 1.0}),
	x3: dict({x0: 1.0}),
      }

# the labeling function
L =   { x0: [CLOSED],
	x1: [OPENING],
	x2: [OPEN],
	x3: [CLOSING]
      }

# define the event function
E =   { x0: [BUTTON_PRESSED],
	x1: [LIMIT_TRIPPED],
	x2: [BUTTON_PRESSED],
	x3: [LIMIT_TRIPPED]
      }

#def get_event(current_state):
	#if current_state == x0 or current_state == x2:
		#return BUTTON
	#return LIMIT_TRIPPED
	
#---- Define the decision function based on LTL formulas.
def hold_properties(current_state, next_state):
	if current_state == x0:
		return next_state == x1
	if current_state == x1:
		return next_state == x2
	if current_state == x2:
		return next_state == x3
	if current_state == x3:
		return next_state == x0

#---- Perform probabilistic state transition, return next state
def transition(current_state):
		return random.choices(  list(R[current_state].keys()),
					list(R[current_state].values()), k=1)[0]

#---- Simulate state transitions
def simulate( initial_state, num_steps):
	current_state = initial_state
	print("Starting in state:", current_state)
	for step in range(1, num_steps):
		next_state = transition(current_state)
		print("Step", step, " ", E[current_state], ": Transition from ", L[current_state]," to ", L[next_state])
		if not hold_properties(current_state, next_state):
			print("Property violated.")
			print("Counterexample: ", L[current_state], " -> ", L[next_state], " (violation)")
			return
		current_state = next_state

#================================================================

simulate( x0, 100 ) # initial state is CLOSED, simulate for 100 transitions
