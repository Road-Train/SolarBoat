public final class Event {
    private Component component;
    private float value;
    private long nanos;

    public Component getComponent() { return component; }

    public float getValue() { return value; }

    public long getNanos() { return nanos; }

    public void set(Component component, float value, long nanos) {
        this.component = component;
        this.value = value;
        this.nanos = nanos;
    }

    public void set(Event other) {
        this.set(other.getComponent(), other.getValue(), other.getNanos());
    }

    /**
     * Return the time the event happened in nanoseconds
     * Can be used to compare with other event times.
     */
    public String toString() {
        return "Event: " + component + ": " + value + " in " + nanos + " nanoseconds.";
    }
}