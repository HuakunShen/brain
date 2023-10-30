package creational_patterns.factory_method;

public class ALinkDOM extends DOM {
    @Override
    public HTMLElement createElement() {
        return new ALinkElement("https://huakunshen.com", "Link to Huakun's website");
    }
}
