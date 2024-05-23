import java.lang.reflect.Type;

public class DefaultControllerEnvironment extends ControllerEnvironment {
    @Override
    public Controller getControllers() {
        return new Controller();
    }
    // A default controller environment
    private Controller controller;

    public Controller getControllers() {
        if(controller == null) {
            controller = new Controller() {
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
        return controller;
    }
}