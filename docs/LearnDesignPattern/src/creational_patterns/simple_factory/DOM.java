package creational_patterns.simple_factory;

public class DOM {
    public static HTMLElement createElement(String type) {
        if (type.equals("a")) {
            return new ALinkElement("https://huakunshen.com", "Huakun's Website");
        } else if (type.equals("p")) {
            return new ParagraphElement("This is a paragraph");
        } else {
            System.out.println("Element Type Not Found");
            return null;
        }
    }

    public static ALinkElement get_a_link() {
        return new ALinkElement("https://huakunshen.com", "Huakun's Website");
    }

    public static ParagraphElement get_paragraph() {
        return new ParagraphElement("This is a paragraph");
    }
}
