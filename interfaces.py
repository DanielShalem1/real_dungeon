import abc


class NPC_interface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'interact') and
                callable(subclass.interact) or NotImplemented)

    @abc.abstractmethod
    def interact(self):
        """
        all NPC need to have basic interaction
        """
        raise NotImplementedError

class item(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'name') and
                hasattr(subclass, 'description') or NotImplemented)

    @abc.abstractmethod
    def active_effect(self):
        """
        all items to have basic active effect
        """
        raise NotImplementedError
