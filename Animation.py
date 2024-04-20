'''

Animation Utils

Created By: Richard Schmidt
Github: ScRichard
Last update: 20.4. 2024

'''

import time
import math

# Every calculation is copied from easings.net
class AnimationType:
    PI = 3.141592653589793238462643383279502884197

    def __init__(self):
        pass

    def execute(self, x: float):
        return x

class EaseInSine(AnimationType):
    def execute(self, t):
        return math.sin(1.5707963 * t)

class EaseOutSine(AnimationType):
    def execute(self, t):
        return 1 + math.sin(1.5707963 * (t - 1))

class EaseInOutSine(AnimationType):
    def execute(self, t):
        return 0.5 * (1 + math.sin(3.1415926 * (t - 0.5)))

class EaseInQuad(AnimationType):
    def execute(self, t):
        return t * t

class EaseOutQuad(AnimationType):
    def execute(self, t):
        return t * (2 - t)

class EaseInOutQuad(AnimationType):
    def execute(self, t):
        return 2 * t * t if t < 0.5 else t * (4 - 2 * t) - 1

class EaseInCubic(AnimationType):
    def execute(self, t):
        return t * t * t

class EaseOutCubic(AnimationType):
    def execute(self, t):
        return 1 + (t - 1) * (t - 1) * (t - 1)

class EaseInOutCubic(AnimationType):
    def execute(self, t):
        return 4 * t * t * t if t < 0.5 else 1 + (t - 1) * (2 * (t - 1)) * (2 * t)

class EaseInQuart(AnimationType):
    def execute(self, t):
        return t * t * t * t

class EaseOutQuart(AnimationType):
    def execute(self, t):
        t -= 1
        return 1 - t * t * t * t

class EaseInOutQuart(AnimationType):
    def execute(self, t):
        if t < 0.5:
            return 8 * t * t * t * t
        else:
            t = 2 * t - 2
            return 1 - 8 * t * t * t * t

class EaseInQuint(AnimationType):
    def execute(self, t):
        return t * t * t * t * t

class EaseOutQuint(AnimationType):
    def execute(self, t):
        t -= 1
        return 1 + t * t * t * t * t

class EaseInOutQuint(AnimationType):
    def execute(self, t):
        if t < 0.5:
            return 16 * t * t * t * t * t
        else:
            t = 2 * t - 2
            return 1 + 16 * t * t * t * t * t

class EaseInExpo(AnimationType):
    def execute(self, t):
        return (2 ** (8 * t) - 1) / 255

class EaseOutExpo(AnimationType):
    def execute(self, t):
        return 1 - 2 ** (-8 * t)

class EaseInOutExpo(AnimationType):
    def execute(self, t):
        if t < 0.5:
            return (2 ** (16 * t) - 1) / 510
        else:
            return 1 - 0.5 * 2 ** (-16 * (t - 0.5))

class EaseInCirc(AnimationType):
    def execute(self, t):
        return 1 - math.sqrt(1 - t)

class EaseOutCirc(AnimationType):
    def execute(self, t):
        return math.sqrt(t)

class EaseInOutCirc(AnimationType):
    def execute(self, t):
        if t < 0.5:
            return (1 - math.sqrt(1 - 2 * t)) * 0.5
        else:
            return (1 + math.sqrt(2 * t - 1)) * 0.5

class EaseInBack(AnimationType):
    def execute(self, t):
        return t * t * (2.70158 * t - 1.70158)

class EaseOutBack(AnimationType):
    def execute(self, t):
        t -= 1
        return 1 + t * t * (2.70158 * t + 1.70158)

class EaseInOutBack(AnimationType):
    def execute(self, t):
        if t < 0.5:
            return t * t * (7 * t - 2.5) * 2
        else:
            t -= 1
            return 1 + t * t * (2 * (7 * t) + 2.5)

class EaseInElastic(AnimationType):
    def execute(self, t):
        t2 = t * t
        return t2 * t2 * math.sin(t * self.PI * 4.5)

class EaseOutElastic(AnimationType):
    def execute(self, t):
        t2 = (t - 1) * (t - 1)
        return 1 - t2 * t2 * math.cos(t * self.PI * 4.5)

class EaseInOutElastic(AnimationType):
    def execute(self, t):
        if t < 0.45:
            t2 = t * t
            return 8 * t2 * t2 * math.sin(t * self.PI * 9)
        elif t < 0.55:
            return 0.5 + 0.75 * math.sin(t * self.PI * 4)
        else:
            t2 = (t - 1) * (t - 1)
            return 1 - 8 * t2 * t2 * math.sin(t * self.PI * 9)

class EaseInBounce(AnimationType):
    def execute(self, t):
        return 2 ** (6 * (t - 1)) * abs(math.sin(t * self.PI * 3.5))

class EaseOutBounce(AnimationType):
    def execute(self, t):
        return 1 - 2 ** (-6 * t) * abs(math.cos(t * self.PI * 3.5))

class EaseInOutBounce(AnimationType):
    def execute(self, t):
        if t < 0.5:
            return 8 * 2 ** (8 * (t - 1)) * abs(math.sin(t * self.PI * 7))
        else:
            return 1 - 8 * 2 ** (-8 * t) * abs(math.sin(t * self.PI * 7))

# Creating animation it self -> is between 0 - 1
class Animation:
    def __init__(self, millis : float, animationType):
        self.millis = millis
        self.reversed = False
        self.lastReversed = True
        self.animationType = animationType

        self.start_timer = time.time()*1000
    def get(self):
        if self.reversed != self.lastReversed:
            self.reset()
            a = 1
            if self.lastReversed:
                a = 0
            self.lastReversed = self.reversed
            return a
        else:
            if self.get_time_difference() >= 1:
                a = 1
                if self.reversed:
                    a = 0
                return a
        self.lastReversed = self.reversed

        if self.reversed:
            return 1-self.animationType.execute(t=self.get_time_difference())
        return self.animationType.execute(t=self.get_time_difference())

    def get_time_difference(self):
        return float(time.time()*1000 - self.start_timer) / self.millis
    def is_finished(self):
        return self.get_time_difference() >= 1
    def reset(self):
        self.start_timer = time.time()*1000