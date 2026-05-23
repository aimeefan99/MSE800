# Factory Pattern

GitHub link: https://github.com/aimeefan99/MSE800

File: `MSE800-PSD/Week7/Demo/factory_pattern.py`

This file is a sample of the Factory Design Pattern. The idea of this pattern is to use a factory to create objects instead of creating them directly in the client code.

There are classes and subclasses in this code.

- `Factory` is the parent class
- `AnimalFactory`, `DogFactory`, and `CatFactory` are subclasses of `Factory`
- `Animals` is the parent class
- `Dog` and `Cat` are subclasses of `Animals`

## Why the original code gives an error

In the original code, `DogFactory.create_product()` only has:

```python
def create_product(self, kind=None):
    pass
```

`pass` means the method does nothing. Because there is no `return` statement, Python returns `None`.

In the client code:

```python
factory = DogFactory()
dog = Dog()
dog = factory.create_product()

dog.run()
```

At first, `dog = Dog()` creates a `Dog` object. But the next line:

```python
dog = factory.create_product()
```

replaces `dog` with the result of `create_product()`. Since `create_product()` returns `None`, `dog` becomes `None`.

So when the program runs:

```python
dog.run()
```

it gives this error:

```python
AttributeError: 'NoneType' object has no attribute 'run'
```

## How to fix it

To make the code work, `DogFactory` should return a real `Dog` object:

```python
class DogFactory(Factory):
    
    def create_product(self, kind=None):
        return Dog()
```

`CatFactory` can also be fixed in the same way:

```python
class CatFactory(Factory):
    
    def create_product(self, kind=None):
        return Cat()
```

Another simple way is to comment out:

```python
dog = factory.create_product()
```

Then the client code keeps the object created by:

```python
dog = Dog()
```

So `dog.run()` works. This makes the script run, but it does not really use the factory to create the object.

## Outcome after the fix

After changing `pass` to `return Dog()`, the factory can create a real `Dog` object. Then `dog.run()` will work successfully and the output will be:

```python
I'm a Dog, I can run!!
```

So, the original file shows the structure of the Factory Pattern, but it is incomplete. After returning a real object from the factory method, the program works correctly.

If both factory methods are changed and the client code uses the factory directly:

```python
# client
factory = DogFactory()
dog = factory.create_product()
dog.run()

factory = CatFactory()
cat = factory.create_product()
cat.run()
```

the program runs successfully with this output:

```python
I'm a Dog, I can run!!
I'm a Cat, I can run!!
```

This is the correct way to use the Factory Pattern in this example, because the objects are created by the factory, not directly by `Dog()` or `Cat()`.
