from . import BlackScholesCall, BlackScholesPut ,Black76Call, Black76Put
from .base import BlackScholesStructureBase, Black76StructureBase


class BlackScholesButterflyLong(BlackScholesStructureBase):
    """
    Create long butterfly option structure.
    - Long butterfly -> Call(K1) - 2 * Call(K2) + Call(K3)

    :param S: Price of underlying asset \n
    :param K1: Strike price for 1st option \n
    :param K2: Strike price for 2nd option \n
    :param K3: Strike price for 3rd option \n
    It must hold that K1 < K2 < K3. \n
    Additionally, it must hold that K2 - K1 = K3 - K2 \n
    :param T: Time till expiration in years (1/12 indicates 1 month) \n
    :param r: Risk-free interest rate (0.05 indicates 5%) \n
    :param sigma: Volatility (standard deviation) of stock (0.15 indicates 15%) \n
    :param q: Annual dividend yield (0.05 indicates 5% yield)
    """

    def __init__(
        self,
        S: float,
        K1: float,
        K2: float,
        K3: float,
        T: float,
        r: float,
        sigma: float,
        q: float = 0.0,
    ):
        assert (
            K1 < K2 < K3
        ), f"""It must hold that K1 < K2 < K3.
                        Got {K1}, {K2} and {K3}.
                        """
        assert (
            K2 - K1 == K3 - K2
        ), f"""Strike price must be symmetric, so K2 - K1 = K3 - K2.
                        Got {K2}-{K1} != {K3}-{K2}.
                        """
        super().__init__()
        self.call1 = BlackScholesCall(S=S, K=K1, T=T, r=r, sigma=sigma, q=q)
        self.call2 = BlackScholesCall(S=S, K=K2, T=T, r=r, sigma=sigma, q=q)
        self.call3 = BlackScholesCall(S=S, K=K3, T=T, r=r, sigma=sigma, q=q)

    def _calc_attr(self, attribute_name: str) -> float:
        """
        Combines attributes from three call options into a long call butterfly. \n
        All greeks and price are combined in the same way.

        :param attribute_name: String name of option attribute
        pointing to a method that can be called on
        BlackScholesCall and BlackScholesPut.

        :return: Combined value according to long call butterfly.
        """
        call_attr1 = getattr(self.call1, attribute_name)
        call_attr2 = getattr(self.call2, attribute_name)
        call_attr3 = getattr(self.call3, attribute_name)
        return call_attr1() - 2 * call_attr2() + call_attr3()


class BlackScholesButterflyShort(BlackScholesStructureBase):
    """
    Create short butterfly option structure. \n
    - Short butterfly -> -Put(K1) + 2 * Put(K2) - Put(K3)

    :param S: Price of underlying asset \n
    :param K1: Strike price for 1st option \n
    :param K2: Strike price for 2nd option \n
    :param K3: Strike price for 3rd option \n
    It must hold that K1 < K2 < K3. \n
    Additionally, it must hold that K2 - K1 = K3 - K2 \n
    :param T: Time till expiration in years (1/12 indicates 1 month) \n
    :param r: Risk-free interest rate (0.05 indicates 5%) \n
    :param sigma: Volatility (standard deviation) of stock (0.15 indicates 15%) \n
    :param q: Annual dividend yield (0.05 indicates 5% yield)
    """

    def __init__(
        self,
        S: float,
        K1: float,
        K2: float,
        K3: float,
        T: float,
        r: float,
        sigma: float,
        q: float = 0.0,
    ):
        assert (
            K1 < K2 < K3
        ), f"""It must hold that K1 < K2 < K3.
                        Got {K1}, {K2} and {K3}.
                        """
        assert (
            K2 - K1 == K3 - K2
        ), f"""Strike price must be symmetric, so K2 - K1 = K3 - K2.
                        Got {K2}-{K1} != {K3}-{K2}.
                        """
        super().__init__()
        self.put1 = BlackScholesPut(S=S, K=K1, T=T, r=r, sigma=sigma, q=q)
        self.put2 = BlackScholesPut(S=S, K=K2, T=T, r=r, sigma=sigma, q=q)
        self.put3 = BlackScholesPut(S=S, K=K3, T=T, r=r, sigma=sigma, q=q)

    def _calc_attr(self, attribute_name: str) -> float:
        """
        Combines attributes from three put options into a short put butterfly. \n
        All greeks and price are combined in the same way.

        :param attribute_name: String name of option attribute
        pointing to a method that can be called on
        BlackScholesCall and BlackScholesPut.

        :return: Combined value according to short put butterfly.
        """
        put_attr1 = getattr(self.put1, attribute_name)
        put_attr2 = getattr(self.put2, attribute_name)
        put_attr3 = getattr(self.put3, attribute_name)
        return -put_attr1() + 2 * put_attr2() - put_attr3()


class Black76ButterflyLong(Black76StructureBase):
    """
    Create long butterfly option structure.
    - Long butterfly -> Call(K1) - 2 * Call(K2) + Call(K3)

    :param S: Price of underlying asset \n
    :param K1: Strike price for 1st option \n
    :param K2: Strike price for 2nd option \n
    :param K3: Strike price for 3rd option \n
    It must hold that K1 < K2 < K3. \n
    Additionally, it must hold that K2 - K1 = K3 - K2 \n
    :param T: Time till expiration in years (1/12 indicates 1 month) \n
    :param r: Risk-free interest rate (0.05 indicates 5%) \n
    :param sigma: Volatility (standard deviation) of stock (0.15 indicates 15%) \n
    :param q: Annual dividend yield (0.05 indicates 5% yield)
    """

    def __init__(
        self,
        F: float,
        K1: float,
        K2: float,
        K3: float,
        T: float,
        r: float,
        sigma: float,
        q: float = 0.0,
    ):
        assert (
            K1 < K2 < K3
        ), f"""It must hold that K1 < K2 < K3.
                        Got {K1}, {K2} and {K3}.
                        """
        assert (
            K2 - K1 == K3 - K2
        ), f"""Strike price must be symmetric, so K2 - K1 = K3 - K2.
                        Got {K2}-{K1} != {K3}-{K2}.
                        """
        super().__init__()
        self.call1 = Black76Call(F=F, K=K1, T=T, r=r, sigma=sigma)
        self.call2 = Black76Call(F=F, K=K2, T=T, r=r, sigma=sigma)
        self.call3 = Black76Call(F=F, K=K3, T=T, r=r, sigma=sigma)

    def _calc_attr(self, attribute_name: str) -> float:
        """
        Combines attributes from three call options into a long call butterfly. \n
        All greeks and price are combined in the same way.

        :param attribute_name: String name of option attribute
        pointing to a method that can be called on
        BlackScholesCall and BlackScholesPut.

        :return: Combined value according to long call butterfly.
        """
        call_attr1 = getattr(self.call1, attribute_name)
        call_attr2 = getattr(self.call2, attribute_name)
        call_attr3 = getattr(self.call3, attribute_name)
        return call_attr1() - 2 * call_attr2() + call_attr3()


class Black76ButterflyShort(Black76StructureBase):
    """
    Create short butterfly option structure. \n
    - Short butterfly -> -Put(K1) + 2 * Put(K2) - Put(K3)

    :param S: Price of underlying asset \n
    :param K1: Strike price for 1st option \n
    :param K2: Strike price for 2nd option \n
    :param K3: Strike price for 3rd option \n
    It must hold that K1 < K2 < K3. \n
    Additionally, it must hold that K2 - K1 = K3 - K2 \n
    :param T: Time till expiration in years (1/12 indicates 1 month) \n
    :param r: Risk-free interest rate (0.05 indicates 5%) \n
    :param sigma: Volatility (standard deviation) of stock (0.15 indicates 15%) \n
    :param q: Annual dividend yield (0.05 indicates 5% yield)
    """

    def __init__(
        self,
        F: float,
        K1: float,
        K2: float,
        K3: float,
        T: float,
        r: float,
        sigma: float,
        q: float = 0.0,
    ):
        assert (
            K1 < K2 < K3
        ), f"""It must hold that K1 < K2 < K3.
                        Got {K1}, {K2} and {K3}.
                        """
        assert (
            K2 - K1 == K3 - K2
        ), f"""Strike price must be symmetric, so K2 - K1 = K3 - K2.
                        Got {K2}-{K1} != {K3}-{K2}.
                        """
        super().__init__()
        self.put1 = Black76Put(F=F, K=K1, T=T, r=r, sigma=sigma)
        self.put2 = Black76Put(F=F, K=K2, T=T, r=r, sigma=sigma)
        self.put3 = Black76Put(F=F, K=K3, T=T, r=r, sigma=sigma)

    def _calc_attr(self, attribute_name: str) -> float:
        """
        Combines attributes from three put options into a short put butterfly. \n
        All greeks and price are combined in the same way.

        :param attribute_name: String name of option attribute
        pointing to a method that can be called on
        BlackScholesCall and BlackScholesPut.

        :return: Combined value according to short put butterfly.
        """
        put_attr1 = getattr(self.put1, attribute_name)
        put_attr2 = getattr(self.put2, attribute_name)
        put_attr3 = getattr(self.put3, attribute_name)
        return -put_attr1() + 2 * put_attr2() - put_attr3()
