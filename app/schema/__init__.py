import graphene


class HelloMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String()

    message = graphene.String()

    @classmethod
    def mutate(cls, root, info, name="World!"):
        return HelloMutation(message=f"Hello {name}!")

class HelloQuery(graphene.ObjectType):
    hello = graphene.String()

    def resolve_hello(self, info):
        return "Hello World"

class RootQuery(
    HelloQuery,
    graphene.ObjectType
):
    node = graphene.relay.Node.Field()

class RootMutation(graphene.ObjectType):
    hello = HelloMutation.Field()


schema = graphene.Schema(query=RootQuery, mutation=RootMutation)
