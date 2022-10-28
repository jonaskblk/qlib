"""Contains definition for type Vector and VectorValidator.
"""

from .common import CommonValidator


class Vector:
    """Defines instances of type vector.

    Returns:
        _type_: vector
    """

    def __init__(self, components: list) -> None:
        self.__vector_validator = VectorValidator()
        self.__set_components(components)

    def __set_components(self, components) -> None:
        self.__vector_validator.guard_components_not_empty(components)
        self.__vector_validator.guard_components_of_type_float_or_int(
            components)
        self.__components = [float(index) for index in components]

    def __eq__(self, other: 'object') -> bool:
        self.__vector_validator.guard_is_of_type_vector(other)
        return self.__components.__eq__(other.get_components())  # type: ignore

    def __str__(self) -> str:
        return self.__components.__str__()

    def __repr__(self) -> str:
        return f"Vector({self.__components.__str__()})"

    def get_components(self) -> list:
        """Returns the components of a vector instance as a list.
        """
        return self.__components

    def get_component_by_index(self, index: int) -> float:
        """Returns the value of a single component specified by a given index.

        Args:
            index (int): Index of component greater than 0

        Returns:
            float: Value of component at given index
        """
        self.__vector_validator.guard_index_greater_then_zero(index)
        return self.__components[index - 1]

    def set_value_of_component(self, index: int, value: float) -> None:  # type: ignore
        """Sets the value of a single component specified by a given index.

        Args:
            index (int): Index of the manipulated component greatar than 0
            value (float): New Value of the component
        """
        self.__vector_validator.guard_index_greater_then_zero(index)

        self.__components[index - 1] = value

    def get_number_of_components(self) -> int:
        """Gets the number components.

        Returns:
            int: Number of components.
        """
        return int(len(self.__components))

    def add(self, vector_b: 'Vector') -> None:
        """Adds up two vectors componentwise.

        Args:
            vector_b (Vector): Vector that should be added
        """
        vector_a = Vector(self.__components)
        self.__vector_validator.guard_equal_length_of_components(
            vector_a, vector_b)
        self.__components = [
            a_i + b_i for a_i, b_i in zip(vector_a.get_components(), vector_b.get_components())]

    def subtract(self, vector_b: 'Vector'):
        """Subtracts one vector to from the other componentwise.

        Args:
            vector_b (Vector): Vector that should be subtracted
        """
        vector_a = Vector(self.__components)
        self.__vector_validator.guard_equal_length_of_components(
            vector_a, vector_b)
        self.__components = [
            a_i - b_i for a_i, b_i in zip(vector_a.get_components(), vector_b.get_components())]

    def multiply_with_scalar(self, scalar: float) -> None:
        """Multiplys a vector componentwise with a given scalar.

        Args:
            scalar (float): Number which the components get multiplied with
        """
        self.__vector_validator.guard_is_a_number(scalar)
        vector = Vector(self.__components)
        new_components = [index * scalar for index in vector.get_components()]
        self.__set_components(new_components)

    def sum_of_squares(self) -> float:  # type: ignore
        pass

    def magnitude(self) -> float:  # type: ignore
        pass

    def distance(self, vector_b: 'Vector') -> float:  # type: ignore
        pass

    def squared_distance(self, vector_b: 'Vector') -> float:  # type: ignore
        pass

    @ staticmethod
    def sum_up_vectors(vectors: list['Vector']) -> 'Vector':  # type: ignore
        """Sums up a list of vectors componentwise.

        Args:
            vectors (list[&#39;Vector&#39;]): Vector-list of interest

        Returns:
            Vector: Summed up vectors as a new vector
        """
        vector_validator = VectorValidator()
        vector_validator.guard_list_of_vectors_not_empty(vectors)
        vector_validator.guard_equal_length_of_components_in_list(vectors)

        number_of_components = vectors[0].get_number_of_components()

        sum_of_components = []
        for i in range(number_of_components):
            for vector in vectors:
                value_of_component = vector.get_component_by_index(i + 1)
                sum_of_components[number_of_components] += value_of_component

        return Vector(sum_of_components)

    @ staticmethod
    def mean_of_vectors(vectors: list['Vector']) -> 'Vector':  # type: ignore
        """Calculates the mean of a list of vectors componentwise.

        Args:
            vectors (list[&#39;Vector&#39;]): Vector-list of interests

        Returns:
            Vector: Mean of vectors as a new vector
        """
        vector_validator = VectorValidator()
        vector_validator.guard_list_of_vectors_not_empty(vectors)
        vector_validator.guard_equal_length_of_components_in_list(vectors)

        number_of_vectors = len(vectors)
        sum_of_vectors = Vector.sum_up_vectors(vectors)
        sum_of_vectors.multiply_with_scalar(1/number_of_vectors)
        return sum_of_vectors


class VectorValidator:
    def __init__(self) -> None:
        self.common_validator = CommonValidator()

    def guard_components_not_empty(self, components: list) -> None:
        if (components == []):
            raise Exception("A Vector consists of at least one component")

    def guard_components_of_type_float_or_int(self, components: list) -> None:
        if (all([isinstance(component, float) for component in components])):
            pass
        elif (all([isinstance(component, int) for component in components])):
            pass
        else:
            raise ValueError("Components must be of type float or int")

    def guard_is_of_type_vector(self, object_to_check: object) -> None:
        if not (isinstance(object_to_check, Vector)):
            raise ValueError("Object must be of type vector")

    def guard_index_greater_then_zero(self, index) -> None:
        if not index > 0:
            raise ValueError("Index must be greater then 0")

    def guard_equal_length_of_components(self, vector_a: Vector, vector_b: Vector) -> None:
        if not len(vector_a.get_components()) == len(vector_b.get_components()):
            raise Exception("Vectors must be of the same length")

    def guard_equal_length_of_components_in_list(self, vectors: list[Vector]) -> None:
        awaited_length_of_components = len(vectors[0].get_components())
        if not all(len(i.get_components()) == awaited_length_of_components for i in vectors):
            raise Exception("Vectors must be of the same length")

    def guard_is_a_number(self, input_of_random_type) -> None:
        try:
            self.common_validator.guard_is_a_number(input_of_random_type)
        except ValueError as value_error:
            raise value_error

    def guard_list_of_vectors_not_empty(self, list_of_vectors: list[Vector]) -> None:
        if (list_of_vectors == []):
            raise Exception("The list of vectors can not be empty")
