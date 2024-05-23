import net.java.games.input.Component;
import net.java.games.input.Controller;
import net.java.games.input.ControllerEnvironment;
import net.java.games.input.Event;
import net.java.games.input.EventQueue;

public static class TestController implements Runnable {
    private Controller xBox;

    public TestController(Controller xBox) {
        this.xBox = xBox;
    }

        @Override
        public void run() {
            while (true) {
                xBox.poll();
                EventQueue queue = xBox.getEventQueue();
                Event event = new Event();

                while (queue.getNextEvent(event)) {
                    StringBuffer buffer = new StringBuffer(xBox.getName());
                    buffer.append(" at ");
                    buffer.append(event.getNanos()).append(", ");
                    Component comp = event.getComponent();
                    buffer.append(comp.getName()).append(" changed to ");
                    float value = event.getValue();

                    // check the type of the component and display a value
                    if (comp.isAnalog()) {
                        buffer.append(value);
                    } else {
                        if (value == 1.0f) {
                            buffer.append("On");
                        } else {
                            buffer.append("Off");
                        }
                    }
                    System.out.println(buffer);
                }
                // sleep for 20 ms, the example does not trash the system
                try {
                    Thread.sleep(20);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }
    }

    public static void main(String[] args) {
        System.out.println("Welcome To The Console World!");
        System.out.println("Introducing by the Solar Boat team");

        // Get the default controller environment
        // ControllerEnvironment represents a collection of controllers
        // that are physically / logically linked
        // by default, this correspons to the environment for the local machine
        ControllerEnvironment controllerEnvironment;
        controllerEnvironment = ControllerEnvironment.getDefaultEnvironment();

        // Get an array of all the controllers
        Controller[] controllers = controllerEnvironment.getControllers();

        // Iterate over each controller that is connected
        // and print something out
        for (Controller controller : controllers) {
            System.out.println("Controller: " + controller);
            System.out.println(controller.poll()); // poll controller
            System.out.println(controller.getName());
            new Thread(new TestController(controller)).start();
        }
    }