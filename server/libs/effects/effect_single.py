from libs.effects.effect import Effect # pylint: disable=E0611, E0401

import numpy as np

class EffectSingle(Effect):
    def run(self):
        """
        Show one single color.
        """
        # Get the config of the current effect
        effect_config = self._config["effects"]["effect_single"]
        # Build an empty array
        output_array = np.zeros((3, self._config["device_config"]["LED_Count"]))
        
        # Fill the array with the selected color
        output_array[0][:]=self._config_colours[effect_config["color"]][0]
        output_array[1][:]=self._config_colours[effect_config["color"]][1]
        output_array[2][:]=self._config_colours[effect_config["color"]][2]

        # Add the output array to the queue
        self._output_queue_lock.acquire()
        self._output_queue.put(output_array)
        self._output_queue_lock.release()