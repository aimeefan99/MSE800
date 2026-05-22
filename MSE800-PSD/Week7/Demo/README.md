# Factory Pattern

GitHub link: https://github.com/aimeefan99/MSE800

File: `MSE800-PSD/Week7/Demo/factory_pattern.py`

This code is an example of the Factory Design Pattern. It uses a factory to create objects instead of creating them directly.

There are classes and subclasses in the code. `Factory` is the parent class of `AnimalFactory`, `DogFactory`, and `CatFactory`. `Animals` is the parent class of `Dog` and `Cat`.

The expected result is that the factory creates a `Dog` or `Cat`, and then the object can use `run()`.

However, in the current code, `DogFactory.create_product()` only has `pass`, so it does not create anything and returns `None`. Because of that, `dog.run()` gives an error:

`AttributeError: 'NoneType' object has no attribute 'run'`

To make it work, this part can be changed from:

```python
class DogFactory(Factory):
    
    def create_product(self, kind=None):
        pass
```

to:

```python
class DogFactory(Factory):
    
    def create_product(self, kind=None):
        return Dog()
```

After this change, the output will be:

```python
I'm a Dog, I can run!!
```
