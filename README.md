# catkin-cargo

Build cargo based catkin packages.

How to use
----------

Set the build type in package.xml

```xml
<?xml version="1.0"?>
<package format="2">
  <name>...</name>

  <export>
    <build_type>cargo</build_type>
  </export>
</package>
```

Add package to catkin workspace. Then build:

```
catkin build
```
