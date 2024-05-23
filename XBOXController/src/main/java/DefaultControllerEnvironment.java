import java.util.ArrayList;
import java.util.List;

public class DefaultControllerEnvironment extends ControllerEnvironment {
    private List<Controller> controllers;

    public DefaultControllerEnvironment() {
        controllers = new ArrayList<>();
        controllers.add(new XboxController());
    }
    @Override
    public Controller[] getControllers() {
        return controllers.toArray(new Controller[0]);
    }
    // A default controller environment


}