from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    
    def run(self, agent):
        '''
        this method will execute the current state with agent
        '''
        raise NotImplementedError('run method is not implemented ')

    @abstractmethod
    def transition_to(self, agent, state):
        '''
        this method will send the current to next state 
        it will acts as a bridge between two state
        '''
        raise NotImplementedError('transition_to method is not implemenated ..')
