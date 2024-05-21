package org.example;

import net.java.games.input.Component;
import net.java.games.input.Controller;
import net.java.games.input.ControllerEnvironment;

public class PS5ControlTest {

    public static void main(String[] args) {
        // Get the default controller environment
        ControllerEnvironment controllerEnvironment = ControllerEnvironment.getDefaultEnvironment();

        // Get all controllers (including gamepads, joysticks, etc.)
        Controller[] controllers = controllerEnvironment.getControllers();

        // Find the PS5 controller
        Controller ps5Controller = null;
        for (Controller controller : controllers) {
            if (controller.getName().toLowerCase().contains("wireless controller")) {
                ps5Controller = controller;
                break;
            }
        }

        // If PS5 controller is found, start reading inputs
        if (ps5Controller != null) {
            ps5Controller.poll();
            Component[] components = ps5Controller.getComponents();

            // Main loop to continuously read inputs
            while (true) {
                ps5Controller.poll();

                // Read button inputs and print them out to the console
                for (Component component : components) {
                    if (component.isAnalog() || component.isRelative()) {
                        continue; // Skip analog and relative components
                    }

                    if (component.getPollData() == 1.0f) {
                        System.out.println(component.getName() + " pressed");
                    }
                }

                // Add a short delay to prevent high CPU usage
                try {
                    Thread.sleep(100);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        } else {
            System.out.println("PS5 controller not found.");
        }
    }
}