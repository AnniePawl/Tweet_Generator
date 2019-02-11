# COIN EXAMPLE
# Stochastic Sampling Practice

import random

# Probablity Variables
head_probability = 0.3
tail_probability = 0.5
body_probability = 0.2


prob_dict = {
    "heads": head_probability,
    "bodys": body_probability,
    "tails": tail_probability
}

random_point = random.uniform(0, 1)
cum_prob = 0
for outcome in prob_dict:
  cum_prob += prob_dict[outcome]
  if cum_prob > random_point:
    print(outcome)
    break


# ONLY HEAD AND TAILS
#
# 0                        0.3                                                1
# |-------------------------|-------------------------------------------------|
#           heads                                 tails
#


# HEADS, TAILS AND BODY
#
# 0                        0.3              0.5                               1
# |-------------------------|----------------|--------------------------------|
#           heads                  body                    tails
#



# 0                                         0.5             0.7               1
# |------------------------------------------|---------------|----------------|
#                    tails                         body             heads
