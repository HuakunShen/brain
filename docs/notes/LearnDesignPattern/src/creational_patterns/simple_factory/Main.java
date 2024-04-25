package creational_patterns.simple_factory;

public class Main {
    public static void main(String[] args) {
        // Case 1: Use getter method
        HTMLElement a = DOM.get_a_link();
        a.onClick();
        HTMLElement p = DOM.get_paragraph();
        p.onClick();

        // Case 2: Use conditional statements
        a = DOM.createElement("a");
        assert a != null;
        a.render();
        p= DOM.createElement("p");
        assert p != null;
        p.render();
    }
}
