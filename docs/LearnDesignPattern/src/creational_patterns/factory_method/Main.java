package creational_patterns.factory_method;

public class Main {
    public static void main(String[] args) {
        HTMLElement a = new ALinkDOM().createElement();
        a.render();
        a.onClick();
        HTMLElement p = new ParagraphDOM().createElement();
        p.render();
        p.onClick();
    }
}
