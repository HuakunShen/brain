package creational_patterns.simple_factory;


public class ALinkElement implements HTMLElement {
    String href;
    String content;

    public ALinkElement() {
        this.href = "";
        this.content = "";
    }

    public ALinkElement(String href, String content) {
        this.href = href;
        this.content = content;
    }

    public void render() {
        String body = String.format("<a href=\"%s\">%s</a>", this.href, this.content);
        System.out.println(body);
    }

    public void onClick() {
        System.out.println("a link clicked");
    }
}
