# Abstract Factory

## Problem

Suppose there are 3 types of products (families) and each product has 3 variants, then there are 9 products in total.

With regular factory method, we have one factory for each product (in this case, family), but what if we want to add a
new variant without changing existing code?

## Solution

1. Declare an interface for each product family

   Variants of each product family need to implement these interfaces.

2. Declare **AbstractFactory** interface

   It has some methods that return **abstract** product types (family), such as
    - createChair -> Chair
    - createTable -> Table
    - createSofa -> Sofa

3. For each variant of a product family, create a separate factory class based on **AbstractFactory** interface. Each
   factory is responsible for creating the products of a single variant.

4. Client (Application) doesn't need to know which type of factory is used, a concrete factory object could be passed to the application (created beforehand based on some parameters).  

## Sample Code

[Reference](https://refactoring.guru/design-patterns/abstract-factory/java/example)

### Products

```java
// Abstract Button
public interface Button {
    void paint();
}

/**
 * MacOS variant of button
 */
public class MacOSButton implements Button {

    @Override
    public void paint() {
        System.out.println("You have created MacOSButton.");
    }
}

/**
 * Windows variant of button
 */
public class WindowsButton implements Button {

    @Override
    public void paint() {
        System.out.println("You have created WindowsButton.");
    }
}

// Abstract Checkbox
public interface Checkbox {
    void paint();
}

/**
 * MacOS variant of checkbox
 */
public class MacOSCheckbox implements Checkbox {

    @Override
    public void paint() {
        System.out.println("You have created MacOSCheckbox.");
    }
}

/**
 * Windows variant of checkbox
 */
public class WindowsCheckbox implements Checkbox {

    @Override
    public void paint() {
        System.out.println("You have created WindowsCheckbox.");
    }
}
```

### Factory

```java
/**
 * Abstract factory knows about all (abstract) product types.
 */
public interface GUIFactory {
    Button createButton();

    Checkbox createCheckbox();
}

/**
 * Each concrete factory extends basic factory and responsible for creating
 * products of a single variety.
 * MacOSFactory should be able to create MacOS products
 */
public class MacOSFactory implements GUIFactory {

    @Override
    public Button createButton() {
        return new MacOSButton();
    }

    @Override
    public Checkbox createCheckbox() {
        return new MacOSCheckbox();
    }
}

/**
 * Each concrete factory extends basic factory and responsible for creating
 * products of a single variety.
 * WindowsFactory should be able to create Windows products
 */
public class WindowsFactory implements GUIFactory {

    @Override
    public Button createButton() {
        return new WindowsButton();
    }

    @Override
    public Checkbox createCheckbox() {
        return new WindowsCheckbox();
    }
}
```

### Application (Client)

```java
/**
 * Factory users don't care which concrete factory they use since they work with
 * factories and products through abstract interfaces.
 */
public class Application {
    private Button button;
    private Checkbox checkbox;

    public Application(GUIFactory factory) {
        button = factory.createButton();
        checkbox = factory.createCheckbox();
    }

    public void paint() {
        button.paint();
        checkbox.paint();
    }
}
```

### Demo
```java
/**
 * Demo class. Everything comes together here.
 */
public class Demo {

    /**
     * Application picks the factory type and creates it in run time (usually at
     * initialization stage), depending on the configuration or environment
     * variables.
     */
    private static Application configureApplication() {
        Application app;
        GUIFactory factory;
        String osName = System.getProperty("os.name").toLowerCase();
        if (osName.contains("mac")) {
            factory = new MacOSFactory();
            app = new Application(factory);
        } else {
            factory = new WindowsFactory();
            app = new Application(factory);
        }
        return app;
    }

    public static void main(String[] args) {
        Application app = configureApplication();
        app.paint();
    }
}
```

## Limitation

## Reference

[Guru Abstract Factor](https://refactoring.guru/design-patterns/abstract-factory)