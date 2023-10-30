package creational_patterns.factory_method;

public class ParagraphDOM extends DOM {
    @Override
    public HTMLElement createElement() {
        return new ParagraphElement("I am a paragraph");
    }
}
