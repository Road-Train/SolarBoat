import net.java.games.input.Component;
import net.java.games.input.Controller;
import net.java.games.input.ControllerEnvironment;
import net.java.games.input.Event;
import net.java.games.input.EventQueue;

public class ControllerInputReader {
    private static final float DEAD_ZONE = 0.01f;
    private static float lastLeftX = 0.0f;
    private static float lastLeftY = 0.0f;
    private static float lastRightX = 0.0f;
    private static float lastRightY = 0.0f;
    private static float lastLeftTrigger = 0.0f;
    private static float lastRightTrigger = 0.0f;

    private static final String[] PS5_BUTTON_NAMES = {
            "Triangle", "Circle", "Square", "Cross", "Left Thumbstick button", "PS5", 
            "Right Thumbstick button", "Options", "Left Stick", "Right Stick", 
            "R1", "Up", "Down", "Left", "Right", "Pad"
    };

    public static void main(String[] args) {
        while (true) {
            Controller controller = initializeJoystick();
            if (controller != null) {
                System.out.println("Controller found: " + controller.getName());
                while (true) {
                    if (!controller.poll()) {
                        break;
                    }
                    processJoystickEvents(controller);
                    try {
                        Thread.sleep(10);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
            } else {
                System.out.println("No controller connected.");
                try {
                    Thread.sleep(3000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }
    }

    private static Controller initializeJoystick() {
        Controller[] controllers = ControllerEnvironment.getDefaultEnvironment().getControllers();
        for (Controller controller : controllers) {
            if (controller.getType() == Controller.Type.GAMEPAD) {
                return controller;
            }
        }
        return null;
    }

    private static void processJoystickEvents(Controller controller) {
        controller.poll();
        EventQueue queue = controller.getEventQueue();
        Event event = new Event();
        while (queue.getNextEvent(event)) {
            Component comp = event.getComponent();
            float value = event.getValue();
            String componentName = comp.getName();
            
            if (comp.isAnalog()) {
                handleAxis(componentName, value);
            } else {
                handleButton(componentName, value);
            }
        }
    }

    private static void handleAxis(String name, float value) {
        switch (name) {
            case "x":
                if (Math.abs(value - lastLeftX) > DEAD_ZONE) {
                    lastLeftX = value;
                    System.out.println("Left X Axis: " + value);
                }
                break;
            case "y":
                if (Math.abs(value - lastLeftY) > DEAD_ZONE) {
                    lastLeftY = value;
                    System.out.println("Left Y Axis: " + value);
                }
                break;
            case "rx":
                if (Math.abs(value - lastRightX) > DEAD_ZONE) {
                    lastRightX = value;
                    System.out.println("Right X Axis: " + value);
                }
                break;
            case "ry":
                if (Math.abs(value - lastRightY) > DEAD_ZONE) {
                    lastRightY = value;
                    System.out.println("Right Y Axis: " + value);
                }
                break;
            case "z":
                if (Math.abs(value - lastLeftTrigger) > DEAD_ZONE) {
                    lastLeftTrigger = value;
                    System.out.println("Left Trigger: " + value);
                }
                break;
            case "rz":
                if (Math.abs(value - lastRightTrigger) > DEAD_ZONE) {
                    lastRightTrigger = value;
                    System.out.println("Right Trigger: " + value);
                }
                break;
            default:
                break;
        }
    }

    private static void handleButton(String name, float value) {
        int index = getButtonIndex(name);
        if (index >= 0) {
            String buttonName = PS5_BUTTON_NAMES[index];
            if (value == 1.0f) {
                System.out.println(buttonName + " pressed");
            } else {
                System.out.println(buttonName + " released");
            }
        }
    }

    private static int getButtonIndex(String name) {
        switch (name) {
            case "0": return 0;
            case "1": return 1;
            case "2": return 2;
            case "3": return 3;
            case "4": return 4;
            case "5": return 5;
            case "6": return 6;
            case "7": return 7;
            case "8": return 8;
            case "9": return 9;
            case "10": return 10;
            case "11": return 11;
            case "12": return 12;
            case "13": return 13;
            case "14": return 14;
            case "15": return 15;
            default: return -1;
        }
    }
}