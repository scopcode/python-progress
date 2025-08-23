motorcycles = []
print(motorcycles)
motorcycles.append("ducati")
motorcycles.append("honda")
motorcycles.append("yamaha")
print(motorcycles)
motorcycles.insert(0,"suzuki")
print(motorcycles)
del motorcycles[-1]
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
if popped_motorcycle == "honda":
    print("voila! " + popped_motorcycle + " has been popped!")
else:
    print("Didn't work")