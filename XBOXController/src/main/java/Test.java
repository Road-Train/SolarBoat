public class Test
{
    public static void main( String[] args )
    {
        System.out.println( "Welcome To The Console World!" );
        System.out.println("Introducing by the Solar Boat team");

        // Get the default controller environment
        // ControllerEnvironment represents a collection of controlelrs
        // that are physically / logically linked
        // by default, this correspons to the environment for the local machine
        ControllerEnvironment controllerEnvironment;
        controllerEnvironment = ControllerEnvironment.getDefaultEnvironment();

        // Get an array of all the controllers
        Controller[] controllers = controllerEnvironment.getControllers();

        // Iterate over each controller that is connected
        // and print something out
        for(Controller controller : controllers) {
            System.out.println("Controller: " + controller);

            //TODO: Add logic to handle controller input events HERE
        }
    }
}
