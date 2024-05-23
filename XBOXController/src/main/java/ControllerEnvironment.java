import java.util.ArrayList;
import java.util.logging.Logger;
import java.util.logging.Level;

/**
 * A ControllerEnvironment represents a collection of controllers that are
 * physically or logically linked.  By default, this corresponds to the
 * environment for the local machine.
 **/

public abstract class ControllerEnvironment {
    static void log(String msg) {
        Logger.getLogger(ControllerEnvironment.class.getName()).info(msg);
    }
    private static ControllerEnvironment defaultEnvironment = new DefaultControllerEnvironment();

    protected ControllerEnvironment() {
        if(System.getProperty("jinput.loglevel") != null) {
            String loggerName = ControllerEnvironment.class.getPackage().getName();
            Level level = Level.parse(System.setProperty("jinput.loglevel", System.getProperty("jinput.loglevel")));
            Logger.getLogger(loggerName).setLevel(level);
        }
    }
    public static ControllerEnvironment getDefaultEnvironment() {
        return defaultEnvironment;
    }
    public abstract Controller[] getControllers();
}