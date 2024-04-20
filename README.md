# Animation utils (Python)

This library makes using animations easier than before, it's based on easings.net calculations.




```python
# Import a library
import Animation

# I think thats understandable ;)
delay = 100
animationType = Animation.EaseInQuint()

# Create an animation
animation = Animation.Animation(delay, animationType)

# How you can make it reversed, its based on this
animation.reversed = not button.hover()

# Returns calculated value between 0 and 1

print(animation.get())

```

