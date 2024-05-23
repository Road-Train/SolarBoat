package $org.example;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        System.out.println( "Welcome To The Console World!" );
        System.out.println("Introducing by the Solar Boat team");

        // Get the default controller environment
        // ControllerEnvironment represents a collection of controlelrs
        // that are physically / logically linked
        // by default, this correspons to the environment for the local machine
        ControllerEnvironment controllerEnvironment = new ControllerEnvironment();
        controllerEnvironment = ControllerEnvironment.getDefaultEnvironment();

        // Get the controller (only one we need)
        Controller[] controllers = controllerEnvironment.getControllers();

        // Iterate over each controller that is connected
        // and print something out
        if(controller != null)
        {
            System.out.println("Controller: " + controller);

            //TODO: Add logic to handle controller input events HERE
        }
    }
}
