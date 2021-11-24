last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
# Create subjects list
subjects = ['physics', 'calculus', 'poetry', 'history']

# Create grades list
grades = [98, 97, 85, 88]

# Create gradebook
gradebook = [
  ['physics', 98],
  ['calculus', 97],
  ['poetry', 85],
  ['history', 88],
]
print(gradebook)

# Add computer science to gradebook
gradebook.append(['computer science', 100])
print(gradebook)

# Add visual arts to gradebook
gradebook.append(['visual arts', 93])
print(gradebook)

# Add 5 to vis arts grade
gradebook[-1][-1] += 5
print(gradebook)

# remove grade from poetry
gradebook[2].remove(85)
print(gradebook)

# append pass to poetry class
gradebook[2].append("Pass")
print(gradebook)

# Create full_gradebook
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)