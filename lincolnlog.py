"""Lincoln Log Module"""
import names
class LincolnLog:
    """A class representing a Lincoln Log, which can be used to create a simple structure with segments."""
    _rotation = 'horizontal'
    _transform = (0, 0)
    segments = 1  # Default to a single segment
    def __init__(self, length=1, rotation='horizontal', transform=(0, 0)):
        self.name = names.get_full_name()
        self.length = length
        self.rotation = rotation
        self.transform = transform

        # no matter what, our first intersection point is always the transform point
        self.intersection_points = [self.transform]

        # after that, the points depend on the number of segments and rotation
        for i in range(2, self.segments, 2):
            if self.rotation == 'horizontal':
                new_point = (self.transform[0] + i, self.transform[1])
            else:
                new_point = (self.transform[0], self.transform[1] + i)
            self.intersection_points.append(new_point)

    def __str__(self):
        return f"Hello, I am {self.name}, a Lincoln Log with {self.segments} segment{'' if self.segments == 1 else 's'}!"


    @property
    def length(self):
        """Get the length of the Lincoln Log."""
        return (self.segments + 1) // 2

    @length.setter
    def length(self, value):
        """Set the length of the Lincoln Log."""
        if value < 1:
            raise ValueError("Length must be at least 1.")
        self.segments = 1 + 2 * (value - 1)
        self._recalculate_intersection_points()

    @property
    def rotation(self):
        """Get the rotation of the Lincoln Log."""
        return self._rotation

    @rotation.setter
    def rotation(self, value):
        """Set the rotation of the Lincoln Log."""
        if value not in ['horizontal', 'vertical']:
            raise ValueError("Rotation must be either 'horizontal' or 'vertical'.")
        self._rotation = value
        self._recalculate_intersection_points()

    @property
    def transform(self):
        """Get the transform of the Lincoln Log."""
        return self._transform

    @transform.setter
    def transform(self, value):
        """Set the transform of the Lincoln Log."""
        if not isinstance(value, tuple) or len(value) != 2:
            raise ValueError("Transform must be a tuple of (x, y).")
        self._transform = value
        self._recalculate_intersection_points()

    def _recalculate_intersection_points(self):
        """Recalculate intersection points based on new transform
        and rotation."""
        self.intersection_points = [self.transform]
        for i in range(2, self.segments, 2):
            if self.rotation == 'horizontal':
                new_point = (self.transform[0] + i, self.transform[1])
            else:
                new_point = (self.transform[0], self.transform[1] + i)
            self.intersection_points.append(new_point)
