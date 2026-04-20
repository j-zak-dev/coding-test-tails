import type { RichStore, Store } from '../../domain/aggregates/Store'
import type { StoreInterface } from '../../domain/interfaces/storeInterface'

export class StoreService {
  private readonly storeRepository: StoreInterface

  constructor(storeRepository: StoreInterface) {
    this.storeRepository = storeRepository
  }

  async getAllStores(): Promise<Store[]> {
    return this.storeRepository.getAll()
  }

  async searchStoresByName(name: string): Promise<Store[]> {
    const query = name.trim()
    if (!query) {
      return this.getAllStores()
    }
    return this.storeRepository.searchByName(query)
  }

  async getEnrichedStoresByNames(names: string[]): Promise<RichStore[]> {
    const normalizedNames = names
      .map((name) => name.trim())
      .filter((name) => Boolean(name))

    if (normalizedNames.length === 0) {
      return []
    }

    return this.storeRepository.getEnrichedByNames(normalizedNames)
  }
}
