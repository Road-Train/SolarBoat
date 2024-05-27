import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.List;

public class XboxController implements Controller {
    private List<Component> components;

    public XboxController() {
        components = new ArrayList<>();
        // Add Xbox buttons
        components.add(new XboxButton(Component.Identifier.Button.A));
        components.add(new XboxButton(Component.Identifier.Button.B));
        components.add(new XboxButton(Component.Identifier.Button.X));
        components.add(new XboxButton(Component.Identifier.Button.Y));
        components.add(new XboxButton(Component.Identifier.Button.LEFT_THUMB));
        components.add(new XboxButton(Component.Identifier.Button.RIGHT_THUMB));
        components.add(new XboxButton(Component.Identifier.Button.SELECT));
        components.add(new XboxButton(Component.Identifier.Button.START));
        // Add Xbox axes
        components.add(new XboxAxis(Component.Identifier.Axis.X));
        components.add(new XboxAxis(Component.Identifier.Axis.Y));
        components.add(new XboxAxis(Component.Identifier.Axis.RX));
        components.add(new XboxAxis(Component.Identifier.Axis.RY));
    }

    @Override
    public Controller[] getControllers() {
        return new Controller[0];
    }

    @Override
    public Type getType() {
        return null;
    }

    @Override
    public Component[] getComponents() {
        return components.toArray(new Component[0]);
    }

    @Override
    public Component getComponent(Component.Identifier id) {
        for (Component component : components) {
            if (component.getIdentifier().equals(id)) {
                return component;
            }
        }
        return null; // Component not found
    }
}
