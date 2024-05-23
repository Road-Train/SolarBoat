import java.util.ArrayList;
import java.util.List;
import java.lang.reflect.Type;

public class DefaultControllerEnvironment extends ControllerEnvironment {
    private List<Controller> controllers;
    private Controller defaultController;

    public DefaultControllerEnvironment() {
        controllers = new ArrayList<>();
        controllers.add(new XboxController());
    }

    @Override
    public Controller[] getControllers() {
        return controllers.toArray(new Controller[0]);
    }

    public Controller getDefaultController() {
        if (defaultController == null) {
            defaultController = new Controller() {
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
                    return new Component[0];
                }

                @Override
                public Component getComponent(Component.Identifier id) {
                    return null;
                }
            };
        }
        return defaultController;
    }
}
