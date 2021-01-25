import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VennVHLComponent } from './venn-vhl.component';

describe('VennVHLComponent', () => {
  let component: VennVHLComponent;
  let fixture: ComponentFixture<VennVHLComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ VennVHLComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(VennVHLComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
