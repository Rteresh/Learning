from third.die_st.die import Die

# Create die
die = Die()
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)
print(results)
