package creational_patterns.factory_method;

public class ParagraphElement implements HTMLElement {
    String content;

    public ParagraphElement() {
        this.content = "";
    }

    public ParagraphElement(String content) {
        this.content = content;
    }

    public void render() {
        String body = String.format("<p>%s</a>", this.content);
        System.out.println(body);
    }

    public void onClick() {
        System.out.println("paragraph element clicked");
    }
}
