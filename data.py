data = [
  131.8 + 147.7,
  132.1 + 408,
  134.4 + 155.2,
  132.2 + 352.8,
  136.3 + 357.5,
  133 + 344.7,
  133.9 + 176.8,
  141.9 + 175.4,
  134.6 + 151.4,
  132.6 + 165.6
]

# dataの平均
mean = sum(data) / len(data)

# dataの最高
max = max(data)

# dataの最低
min = min(data)

print("\
mean: \t%f ms \t(%f s)\n\
max: \t%f ms \t(%f s)\n\
min: \t%f ms \t(%f s)\
" % (mean, mean / 1000, max, max / 1000, min, min / 1000))
