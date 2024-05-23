/**
 * An axis is a single button, slider or dial which has a single range.
 * Hold information for motion.
 **/

public interface Component {
    Identifier getIdentifier();
    boolean isRelative();
    boolean isAnalog();
    float getDeadZone();
    float getPollData();
    String getName();

    class Identifier {
        private final String name;

        public Identifier(String name) { this.name = name; }
        public String getName() { return name; }
        public String toString() { return name; }
        public static class Axis extends Identifier {
            protected Axis(String name) { super(name); }
            public static final Axis X = new Axis("X");
            public static final Axis Y = new Axis("Y");
            public static final Axis Z = new Axis("Z");
            public static final Axis RX = new Axis("RX");
            public static final Axis RY = new Axis("RY");
            public static final Axis RZ = new Axis("RZ");
            public static final Axis SLIDER = new Axis("SLIDER");
            public static final Axis SLIDER_ACCELERATION = new Axis("SLIDER_ACCELERATION");
            public static final Axis SLIDER_FORCE = new Axis("slider-force");
            public static final Axis SLIDER_VELOCITY = new Axis("slider-velocity");
            public static final Axis X_ACCELERATION = new Axis("x-acceleration");
            public static final Axis X_FORCE = new Axis("x-force");
            public static final Axis X_VELOCITY = new Axis("x-velocity");
            public static final Axis Y_ACCELERATION = new Axis("y-acceleration");
            public static final Axis Y_FORCE = new Axis("y-force");
            public static final Axis Y_VELOCITY = new Axis("y-velocity");
            public static final Axis Z_ACCELERATION = new Axis("z-acceleration");
            public static final Axis Z_FORCE = new Axis("z-force");
            public static final Axis Z_VELOCITY = new Axis("z-velocity");
            public static final Axis RX_ACCELERATION = new Axis("rx-acceleration");
            public static final Axis RX_FORCE = new Axis("rx-force");
            public static final Axis RX_VELOCITY = new Axis("rx-velocity");
            public static final Axis RY_ACCELERATION = new Axis("ry-acceleration");
            public static final Axis RY_FORCE = new Axis("ry-force");
            public static final Axis RY_VELOCITY = new Axis("ry-velocity");
            public static final Axis RZ_ACCELERATION = new Axis("rz-acceleration");
            public static final Axis RZ_FORCE = new Axis("rz-force");
            public static final Axis RZ_VELOCITY = new Axis("rz-velocity");
            public static final Axis POV = new Axis("pov");
            public static final Axis UNKNOWN = new Axis("unknown");
        }
        public static class Button extends Identifier {
            public Button(String name) { super(name); }
            // First device button
            public static final Button _0 = new Button("0");
            public static final Button TRIGGER = new Button("Trigger");
            public static final Button THUMB = new Button("Thumb");
            public static final Button TOP = new Button("Top");
            public static final Button TOP2 = new Button("Top 2");
            public static final Button PINKIE = new Button("Pinkie");
            // Joystick button on the base of the device
            // TO DO: Come back later, might be
            public static final Button BASE = new Button("Base");
            // This is my favourite, from the source:
            // "erm, dunno, but it's in the defines so it might exist."
            public static final Button DEAD = new Button("Dead");
            public static final Button A = new Button("A");
            public static final Button B = new Button("B");
            public static final Button C = new Button("C");
            public static final Button X = new Button("X");
            public static final Button Y = new Button("Y");
            public static final Button Z = new Button("Z");
            public static final Button LEFT_THUMB = new Button("Left Thumb");
            public static final Button RIGHT_THUMB = new Button("Right Thumb");
            public static final Button SELECT = new Button("Select");
            public static final Button START = new Button("Start");
            // Mode button?
            public static final Button MODE = new Button("Mode");

        }
    }
}