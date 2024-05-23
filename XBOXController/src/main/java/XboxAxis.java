public class XboxAxis implements Component {
    private Component.Identifier.Axis identifier;

    public XboxAxis(Component.Identifier.Axis identifier) {
        this.identifier = identifier;
    }

    @Override
    public Component.Identifier.Axis getIdentifier() {
        return identifier;
    }

    @Override
    public boolean isRelative() {
        return false;
    }

    @Override
    public boolean isAnalog() {
        return true;
    }

    @Override
    public float getDeadZone() {
        return 0.1f; // Example dead zone
    }

    @Override
    public float getPollData() {
        return 0.5f;
    }

    @Override
    public String getName() {
        return identifier.getName();
    }
}
