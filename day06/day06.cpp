#include <set>
#include <vector>
#include <iostream>
#include <algorithm>

int findBanksWithMostBlocks(const std::vector<unsigned int> &banks)
{
  return std::distance(banks.begin(), std::max_element(banks.begin(), banks.end()));
}

unsigned int countRedistributionCycles(std::vector<unsigned int> banks)
{
  // TODO: using std::unsigned_set and custom hash for std::vector may help a lot
  std::set< const std::vector<unsigned int> > history = {};
  unsigned int redistributionCyclesCount = 0;

  while (history.find(banks) == history.end()) // run until current bank state is re-encountered
  {
    history.insert(banks);
    int index = findBanksWithMostBlocks(banks);
    unsigned int countToRedistribute = banks[index];
    unsigned int itemsToFillPerBank = countToRedistribute / (unsigned int) (banks.size() - 1);  //floor div
    int banksToFill = banks.size() - 1;
    if (countToRedistribute > 0 && itemsToFillPerBank == 0)
    {
      banksToFill = countToRedistribute;
      itemsToFillPerBank = 1;
    }
    unsigned int itemsToDecreaseAtCurrentBank = banksToFill * itemsToFillPerBank;
    banks[index] = banks[index] - itemsToDecreaseAtCurrentBank;
    for (unsigned int i=1; i<=banksToFill; i++)
    {
      int idx = (index+i) % banks.size();
      banks[idx] += itemsToFillPerBank;
    }

    redistributionCyclesCount++;
  }

  return redistributionCyclesCount;
}

unsigned int getLoopSize(std::vector<unsigned int> banks)
{
  std::vector< const std::vector<unsigned int> > history = {};
  while (std::find(history.begin(), history.end(), banks) == history.end())
  {
    history.push_back(banks);

    int index = findBanksWithMostBlocks(banks);
    unsigned int countToRedistribute = banks[index];
    unsigned int itemsToFillPerBank = countToRedistribute / (unsigned int) (banks.size() - 1);  //floor div
    int banksToFill = banks.size() - 1;
    if (countToRedistribute > 0 && itemsToFillPerBank == 0)
    {
      banksToFill = countToRedistribute;
      itemsToFillPerBank = 1;
    }
    unsigned int itemsToDecreaseAtCurrentBank = banksToFill * itemsToFillPerBank;

    banks[index] = banks[index] - itemsToDecreaseAtCurrentBank;
    for (unsigned int i=1; i<=banksToFill; i++)
    {
      int idx = (index+i) % banks.size();
      banks[idx] += itemsToFillPerBank;
    }
  }

  return std::distance(std::find(history.begin(), history.end(), banks), history.end());
}

int main()
{
  std::vector<unsigned int> testData = {0, 2, 7, 0};
  std::vector<unsigned int> part1Data = {0,5,10,0,11,14,13,4,11,8,8,7,1,4,12,11};
  std::cout << "test1: " << std::endl << countRedistributionCycles(testData) << std::endl;
  std::cout << "part1: " << std::endl << countRedistributionCycles(part1Data) << std::endl;
  std::cout << "test2: " << std::endl << getLoopSize(testData) << std::endl;
  std::cout << "part2: " << std::endl << getLoopSize(part1Data) << std::endl;
  return 0;
}
