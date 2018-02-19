#include <iostream>
#include <math.h>

template <class F, class G>
decltype(auto) compose(F&& f, G&& g)
{
    return [=](auto x) { return f(g(x)); };
}

int main() {
  std::cout << compose(sin, asin)(0.5) << "\n";
  return 0;
}
