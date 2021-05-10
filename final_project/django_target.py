from luigi import Target


class DjangoModelTarget(Target):
    """ Luigi target for Django models """

    def __init__(self, model, **unique):
        """Input args for Django target

        Args:
            model: A Django model
            unique: The keys to target (should only be one field)

        Example:
            target = DjangoModelTarget(Model, unique_key=[1,2,3])
            This will target the values "1, 2, and 3" in field "unique_key" in model "Model"
        """
        self.model = model
        if len(unique) == 1:
            self.unique = unique
        else:
            raise RuntimeError("More than one unique key")

    def get(self):
        return self.model.objects.filter(
            **{f"{key}__in": value for key, value in self.unique.items()}
        )

    def exists(self):
        try:
            m = self.get()
            return (
                True
                if len(m) == len([val for val in self.unique.values()][0])
                else False
            )
        except:
            return False
