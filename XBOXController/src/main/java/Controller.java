import java.awt.*;
import java.lang.reflect.Type;

public interface Controller {
    // Returns the controllers to make up this controller
    // or an empty array if controller contains no child ones.
    Controller[] getControllers();
    // The type of the controller
    Type getType();
    // Returns a components on this controller
    // in order of the assignment priority
    Component[] getComponents();
    // Returns a single axis based on its type
    Component getComponent(Component.Identifier id);

}