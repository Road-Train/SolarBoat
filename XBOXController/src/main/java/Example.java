public class Example {
    public static void main(String[] args) {
        ControllerEnvironment env = ControllerEnvironment.getDefaultEnvironment();
        for (Controller controller : env.getControllers()) {
            System.out.println("Controller: " + controller.getClass().getSimpleName());
            for (Component component : controller.getComponents()) {
                System.out.println("Component: " + component.getName());
            }
        }
    }
}
