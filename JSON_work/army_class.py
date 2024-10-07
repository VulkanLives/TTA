from pandas.core.interchange.dataframe_protocol import DataFrame


class Army():
    def __init__(self, army_in=DataFrame):
        self.input = army_in
        self.costs=[]
        self.costLimits=[]
        self.forces=[]
        self.id=[]
        self.name=[]
        self.battleScribeVersion=[]
        self.generatedBy=[]
        self.gameSystemId=[]
        self.gameSystemName=[]
        self.gameSystemRevision=[]

