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

  async getEnrichedStores(name: string): Promise<RichStore[]> {
    const query = name.trim()
    if (!query) {
      return this.getAllStores()
    }
    return this.storeRepository.getEnrichedByName(query)
  }
}
