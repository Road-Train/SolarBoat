public class XboxButton implements Component {
    private Component.Identifier.Button identifier;

    public XboxButton(Component.Identifier.Button identifier) {
        this.identifier = identifier;
    }

    @Override
    public Component.Identifier.Button getIdentifier() {
        return identifier;
    }

    @Override
    public boolean isRelative() {
        return false;
    }

    @Override
    public boolean isAnalog() {
        return false;
    }

    @Override
    public float getDeadZone() {
        return 0.0f;
    }

    @Override
    public float getPollData() {
        return 1.0f; // Button is pressed
    }

    @Override
    public String getName() {
        return identifier.getName();
    }
}
